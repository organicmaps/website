const fs = require('node:fs');
const path = require('node:path');

const mime = {
  '.html': 'text/html',
  '.js': 'text/javascript',
  '.css': 'text/css',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.webp': 'image/webp',
  '.woff2': 'font/woff2',
  '.ico': 'image/x-icon',
  '.json': 'application/json',
};

function assetResponse(output, pathname) {
  let decoded;
  try {
    decoded = decodeURIComponent(pathname);
  } catch {
    return null;
  }
  const file = path.join(output, decoded, decoded.endsWith('/') ? 'index.html' : '');
  if (file.includes('\0') || !file.startsWith(output + path.sep)) return null;
  if (!fs.statSync(file, { throwIfNoEntry: false })?.isFile()) return null;
  return { body: fs.readFileSync(file), contentType: mime[path.extname(file).toLowerCase()] || 'application/octet-stream' };
}

module.exports = { assetResponse };
