var express = require('express');
var router = express.Router();

var messages = [
  {
    user: "assistant",
    content: "OLA"
  },
  {
    user: "user",
    content: "OLA"
  },
  {
    user: "assistant",
    content: "Lorem ipsum dolor sit amet consectetur adipiscing elit. Consectetur adipiscing elit quisque faucibus ex sapien vitae. Ex sapien vitae pellentesque sem placerat in id. Placerat in id cursus mi pretium tellus duis. Pretium tellus duis convallis tempus leo eu aenean."
  },
  {
    user: "user",
    content: "Lorem ipsum dolor sit amet\n consectetur adipiscing\n elit. Sit amet consectetur\n adipiscing elit quisque faucibus.\n"
  },
  {
    user: "assistant",
    content: "Lorem ipsum dollentesque sem placerat in id. Placerat in id cursus mi pretium tellus duis. Pretium tellus duis convallis tempus leo eu aenean."
  },
]

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express', messages: messages });
});

module.exports = router;
