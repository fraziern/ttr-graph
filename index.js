var pubSub = (function() {
  var callbacks = {};

  return {
    on: (msg, cb) => {
      callbacks[msg] = callbacks[msg] || [];
      callbacks[msg].push(cb);
    },

    publish: (msg, data) => {
      callbacks[msg] = callbacks[msg] || [];
      callbacks[msg].forEach( (cb) => cb(data) );
    }
  };
})();

var pathList = [];

var listToggle = (nodeName) => {
  let idx = pathList.indexOf(nodeName);
  if (idx >= 0) pathList.splice(idx, 1);
  else pathList.push(nodeName);
  pubSub.publish("updateDisplay");
};

pubSub.on("toggle", (nodeName) => {
  let node = document.querySelector("#" + nodeName);
  node.classList.toggle("on");
  listToggle(nodeName);
});

pubSub.on("updateDisplay", () => {
  let output = document.querySelector(".output-text");
  output.textContent = pathList;
});

var components = document.querySelector("#layer3 > *");
components.addEventListener("click", (e) => {
  let id = (e.target && e.target.parentNode) ? e.target.parentNode.id : "";
  if (~id.indexOf("rte")) {
    pubSub.publish("toggle", e.target.parentNode.id);
  }
});
