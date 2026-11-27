const fs = require('node:fs');
const path = require('node:path');

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
  return { path: file };
}

module.exports = { assetResponse };
