const fs = require('fs');

const content = fs.readFileSync('F:\\AntiGravity\\Website\\App\\Schema\\index.html', 'utf8');

// Find the main application script (the last script tag)
const parts = content.split('<script>');
if (parts.length > 1) {
  const lastScript = parts[parts.length - 1].split('</script>')[0];
  fs.writeFileSync('C:\\Users\\Farid\\.gemini\\antigravity\\brain\\4dbfba3b-f74d-4fd0-bdbc-4e1bde065ade\\scratch\\extracted_app.js', lastScript, 'utf8');
  console.log('Main JS extracted, byte length:', lastScript.length);
} else {
  console.error('Could not find script tag');
}
