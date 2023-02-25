import PDFJSExpress from '@pdftron/pdfjs-express'

PDFJSExpress({
  path: '/public/pdfjsexpress',
  licenseKey: 'YOUR_KEY_HERE',
}, document.getElementById('viewer'))
  .then(instance => {
    // use APIs here
  })
