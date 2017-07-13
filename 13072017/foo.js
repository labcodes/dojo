module.exports = function (n) {
  var lights = new Array(n + 1).join('off').split(' ')

  for (var lap = 1; lap <= n; lap++) {
    for (var pos = 1; pos <= n; pos++) {
      if (pos % lap == 0) {
        lights[pos - 1] = switchLight(lights[pos - 1])
      } 
    }
  }

  return lights;
}


function switchLight(light) {
  if (light === 'on'){
    return 'off'
  }
  return 'on'
}