const assert = require('node:assert/strict');
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
  const file = path.join(output, decodeURIComponent(pathname), pathname.endsWith('/') ? 'index.html' : '');
  assert.ok(file.startsWith(output + path.sep), 'Asset path must stay within the build output');
  if (!fs.existsSync(file)) return null;
  return { body: fs.readFileSync(file), contentType: mime[path.extname(file).toLowerCase()] || 'application/octet-stream' };
}

module.exports = { assetResponse };
