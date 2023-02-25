WebViewer({
  licenseKey: 'YOUR_LICENSE_KEY'
}, document.getElementById('viewer'))
  .then(function(instance) {
    var docViewer = instance.docViewer;
    var annotManager = instance.annotManager;
    // call methods from instance, docViewer and annotManager as needed

    // you can also access major namespaces from the instances as follows:
    // var Tools = instance.Core.Tools;
    // var Annotations = instance.Annotations;
  });