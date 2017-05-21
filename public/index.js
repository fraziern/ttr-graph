/*global mina Snap*/
/*eslint no-console: ["error", { allow: ["warn", "error"] }] */
var pathList = [];
var answerList = [];

function calculateRoute(e) {
  e.preventDefault();

  // build JSON
  let routes = pathList.map((path) => {
    let cities = path.replace(/_/g," ").split("-");
    if (cities.length !== 2) {
      console.error("Cities count wrong");
    }
    else return {
      "node1": cities[0],
      "node2": cities[1]
    };
  });

  let JSONOut = { "routes": routes };
  // send JSON
  fetch("/api/longest", {
    method: "POST",
    body: JSON.stringify(JSONOut),
    headers: new Headers({
      "Content-Type": "application/json"
    })
  }).then((json) => json.json())
  .then((data) => {
    displayAnswer(data);
  }).catch((err) => {
    console.error(err);
  });
  // get response, display it
}

function resetGraph() {
  // use pubsub
}

function displayAnswer(data) {
  pubSub.publish("updateDisplay", "Longest Length: " + data.length);

  // generate id names
  answerList = [];
  for (let i = 1; i < data.trail.length; i++) {
    let nodes = [data.trail[i-1], data.trail[i]].sort();
    // TODO change this to a pubsub call
    // that both adds to the answerlist and updates the display
    answerList.push(nodes.join("-").replace(/\s/g, "_"));
  }

  // toggle classes to display answer
  answerList.forEach((nodeName, idx) => {
    let node = document.querySelector("#" + nodeName);
    window.setTimeout(() => {
      animatePath("#" + nodeName);
      node.classList.add("answer");
      node.classList.remove("on");
    }, 500 * idx);
  });
}

function animatePath(gid) {
  let s = Snap(gid);
  let children = s.children();

  for (let i = 0; i < children.length; i++) {
    if (children[i].type == "rect") {
      let box = children[i].getBBox();
      // s.rect(box.x,box.y,box.w, box.h);   // check bounding box
      let matrixStart = children[i].transform().localMatrix;
      let matrixEnd = matrixStart.clone();
      children[i].animate({
        transform: "s1.3 " + matrixEnd.toTransformString()
      }, 200 + 200*i, mina.easeout, () => {
        children[i].animate({
          transform: matrixStart.toTransformString()
        }, 1000);
      });
    }
  }
}

// using pubSub for 2 way data binding
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

// TODO: should this use a set instead?
var listToggle = (nodeName) => {
  let idx = pathList.indexOf(nodeName);
  if (idx >= 0) pathList.splice(idx, 1);
  else pathList.push(nodeName);
  // pubSub.publish("updateDisplay");
};

pubSub.on("toggle", (nodeName) => {
  let node = document.querySelector("#" + nodeName);
  node.classList.toggle("on");
  listToggle(nodeName);
});

pubSub.on("updateDisplay", (content) => {
  let output = document.querySelector(".output-text");
  output.textContent = content;
});

var components = document.querySelectorAll("#svg2 > *");
for (let i = 0; i < components.length; i++) {
  components[i].addEventListener("click", (e) => {
    let id = (e.target && e.target.parentNode) ? e.target.parentNode.id : "";
    pubSub.publish("toggle", id);
  });
}

let btnCalculate = document.querySelector("#btnCalculate");
btnCalculate.addEventListener("click", calculateRoute);
