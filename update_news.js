// This script fetches Telegram channel preview and extracts content from it for our site.
// How content is stored an rendered:
// On disk:
// content/news/2022-01-30/7/index.md  (Telegram ID is used)
// On site:
// /news/2022-01-30/title-text-slug

'use strict';
const channelPreviewUrl = 'https://t.me/s/OrganicMapsApp';
const newsPath = `${__dirname}/content/news/`;

const https = require('https');
const parse = require('node-html-parser').parse;
const fs = require('fs');
const NodeHtmlMarkdown = require('node-html-markdown').NodeHtmlMarkdown;
const nhm = new NodeHtmlMarkdown();
const photoUrlRE = /url\(\'(.*?)\'/;
const emojiRE = /_\*\*(\u00a9|\u00ae|[\u2000-\u3300]\ufe0f?|\ud83c[\ud000-\udfff]|\ud83d[\ud000-\udfff]\ufe0f?|\ud83e[\ud000-\udfff]|\uD83C[\uDDE6-\uDDFF]\uD83C[\uDDE6-\uDDFF])\*\*_/gi;

const kPostsDiffInMs = 10 * 60 * 1000;  // Ten minutes.

function downloadAsync(url, path) {
  return new Promise((resolve, reject) => {
    const request = https.get(url, res => {
      if (res.statusCode != 200) return reject(new Error('statusCode=' + res.statusCode));
      const filePath = fs.createWriteStream(path);
      res.pipe(filePath);
      filePath.on('finish', _ => {
        filePath.close();
        console.log('Downloaded ' + path);
        resolve();
      });
    });
    request.on('error', err => reject(err));
    request.end();
  }).catch(err => console.error('Download failed: ' + err));
}

// Creates a title for news piece from text.
function getTitle(text) {
  // Strip urls and text after them.
  const breakers = ['http', '. ', ':', '\n', '!'];
  for (let b = 0; b < breakers.length; ++b) {
    const i = text.indexOf(breakers[b]);
    if (i > 0) text = text.substring(0, i);
  }
  return text.trim();
}

const dateRE = /-?(\d\d)?\d\d-\d\d-\d\d-?/g;
const slugRE = /(.\ufe0f)?[^\p{L}\p{N}]+/gu;
const kReplacer = '-';
// Removes incompatible symbols from the text. May return an empty string.
function slugify(text) {
  text = text.toLowerCase().replace(slugRE, kReplacer);
  // Remove version numbers (dates) from slugs.
  text = text.replace(dateRE, kReplacer);
  if (text.length && text[0] == kReplacer) text = text.substr(1);
  if (text.length && text[text.length - 1] == kReplacer) text = text.substr(0, text.length - 1);
  return text;
}

const trailingSpacesRE = / +\n/sg;

function toMarkdown(node, date) {
  const time = date.substring(11, 16);
  // News web page title.
  const title = node ? getTitle(node.structuredText) : time;
  let slug = slugify(title);
  if (!slug) slug = time.replace(':', '-');

  const frontmatter = `---\ntitle: "${title.replaceAll("'", "''")}"\ndate: ${date}\nslug: "${slug}"\n---\n\n`;
  // Photo-only posts do not have text, but should have an index.md file.
  if (!node) return frontmatter;

  let content = nhm.translate(node.innerHTML);
  // Clean up some unnecessary whitespaces after nhm conversion.
  content = content.replaceAll(trailingSpacesRE, '\n');
  // We use other dots for lists.
  content = content.replaceAll('• ', '* ');
  // Fix numbered lists like "1\. First".
  content = content.replaceAll(/^(\d+)\\\. /mg, '$1. ');
  // Telegram makes emoji bold italic.
  content = content.replaceAll(emojiRE, '$1');
  return frontmatter + content + '\n'; // Trailing newline for consistency.
}

if (process.argv.length > 2) {
  // Load file from the command line.
  console.log('Loading file ' + process.argv[2]);
  const html = fs.readFileSync(process.argv[2]);
  parseHtml(html);
} else {
  // Download Telegram channel preview html.
  console.log('Downloading ' + channelPreviewUrl);
  const request = https.get(channelPreviewUrl, response => {
    if (response.statusCode != 200) throw new Error('statusCode=' + response.statusCode);
    let chunks = [];
    response.on('data', fragments => chunks.push(fragments));
    response.on('end', _ => {
      const body = Buffer.concat(chunks);
      parseHtml(body.toString());
    });
    response.on('error', err => console.log(err));
  });
  request.on('error', err => console.log(err));
  request.end();
}

function parseHtml(html) {
  const root = parse(html);

  // Skip service messages.
  const messages = root.querySelectorAll('.tgme_widget_message:not(.service_message)');
  console.log('Parsing ' + messages.length + ' Telegram posts.');
  const downloads = [];
  let prevDir;
  let prevDate;
  messages.forEach(m => {
    let photos = m.querySelectorAll('.tgme_widget_message_photo_wrap');
    let text = m.querySelector('.tgme_widget_message_text');
    let date = m.querySelector('time').getAttribute('datetime');
    const id = m.getAttribute('data-post').split('/').pop();

    const yyyyMMdd = date.substring(0, 10);
    const dir = `${newsPath}${yyyyMMdd}/${id}`;;
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
      fs.writeFileSync(dir + '/../_index.md', `---\ndate: ${yyyyMMdd}\nsort_by: date\n---`);
    }

    // Each message may have 0 or more photos.
    for (let i = 1; i <= photos.length; ++i) {
      let photo = photos[i - 1].getAttribute('style');
      photo = photo.match(photoUrlRE)[1];
      const ext = photo.split('.').pop();
      const fileName = `${i}.${ext}`;
      // Handle special cases when image is published as a separate message immediately after
      // the main text message (Telegram has 1024/2048 chars limit for image caption).
      if (!text && prevDate && (new Date(date) - new Date(prevDate)) <= kPostsDiffInMs) {
        // Do not download if images already exist.
        if (!fs.existsSync(`${prevDir}/${i}.png`)
            && !fs.existsSync(`${prevDir}/${i}.webp`)
            && !fs.existsSync(`${prevDir}/${i}.jpg`)
            && !fs.existsSync(`${prevDir}/${i}.jpeg`)) {
          downloads.push(downloadAsync(photo, `${prevDir}/${fileName}`));
          fs.rmSync(dir, { recursive: true, force: true });
        }
      } else {
        downloads.push(downloadAsync(photo, `${dir}/${fileName}`));
      }
    }

    const markdown = toMarkdown(text, date);
    fs.writeFile(`${dir}/index.md`, markdown, err => {
      if (err) console.error(err);
    });

    prevDir = dir;
    prevDate = date;
  });
}
