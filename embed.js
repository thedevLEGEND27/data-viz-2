import file from './map.json' with { type: "json" };
var vlSpec = config
vegaEmbed('#graph2', vlSpec,{"actions": false}).then(function(result) {
  // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);