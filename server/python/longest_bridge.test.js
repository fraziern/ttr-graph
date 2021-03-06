const longestBridge = require('./longest_bridge.js');

var testJSON = {
    "routes": [
        {"node1": "Los Angeles", "node2": "Phoenix"},
        {"node1": "El Paso", "node2": "Phoenix"},
        {"node1": "El Paso", "node2": "Los Angeles"},
        {"node1": "El Paso", "node2": "Santa Fe"},
        {"node1": "Denver", "node2": "Santa Fe"},
        {"node1": "Denver", "node2": "Salt Lake City"},
        {"node1": "Portland", "node2": "Salt Lake City"},
        {"node1": "Portland", "node2": "Seattle"},
        {"node1": "Helena", "node2": "Seattle"},
        {"node1": "Helena", "node2": "Salt Lake City"},
        {"node1": "Helena", "node2": "Duluth"},
        {"node1": "Duluth", "node2": "Omaha"},
        {"node1": "Chicago", "node2": "Omaha"},
        {"node1": "Duluth", "node2": "Toronto"},
        {"node1": "Montreal", "node2": "Toronto"},
        {"node1": "Montreal", "node2": "Sault St. Marie"},
        {"node1": "Duluth", "node2": "Sault St. Marie"},
        {"node1": "Pittsburgh", "node2": "Toronto"},
        {"node1": "Pittsburgh", "node2": "Raleigh"},
        {"node1": "Nashville", "node2": "Raleigh"},
        {"node1": "Nashville", "node2": "Saint Louis"},
        {"node1": "Chicago", "node2": "Saint Louis"}
    ]
};

longestBridge(testJSON, (json) => {
  // json is a stringified json string
  console.log(`typeof: ${typeof json}`);
  console.log(`output: ${json}`);
});
