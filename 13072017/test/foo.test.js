var assert = require('assert');
var switchLights = require('../foo');

describe('foo', function() {
  it('should', function() {
    assert.deepEqual(switchLights(1), ['on']);
    assert.deepEqual(switchLights(2), ['on', 'off']);
    assert.deepEqual(switchLights(3), ['on', 'off', 'off']);
    assert.deepEqual(switchLights(4), ['on', 'off', 'off', 'on']);
    assert.deepEqual(switchLights(5), ['on', 'off', 'off', 'on', 'off']);
    assert.deepEqual(switchLights(6), ['on', 'off', 'off', 'on', 'off', 'off']);
  });
});