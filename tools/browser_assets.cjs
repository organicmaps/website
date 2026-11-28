const fs = require('node:fs');
const path = require('node:path');

// Map a request path to a built file for Playwright, or return null for a 404 response.
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
