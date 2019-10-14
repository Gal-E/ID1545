
alert('this is working!');


var ProgressBar = requirejs('progressbar.js');
var line = new ProgressBar.Line('#container');

var bar = new ProgressBar.Circle(container, {
  strokeWidth: 6,
  easing: 'easeInOut',
  duration: 1400,
  color: '#FFEA82',
  trailColor: '#eee',
  trailWidth: 1,
  svgStyle: null
});

bar.animate(1.0);
