var assert = require('assert');
var detetive = require('../foo.js');
var testarTeoria = detetive.testarTeoria;
var descobrirTeoria = detetive.descobrirTeoria;

describe('Foo', function() {
  it('should return 0 when the theory is correct', function() {
    assert.equal(testarTeoria({s:0, l:1, a:2}, {s:0, l:1, a:2}), 0);
  });

  it('should return 1 when the suspect is incorrect', function() {
    assert.equal(testarTeoria({s:1, l:1, a:2}, {s:0, l:1, a:2}), 1);
    assert.equal(testarTeoria({s:2, l:1, a:2}, {s:0, l:1, a:2}), 1);
  });

  it('should return 2 when the place is incorrect', function() {
    assert.equal(testarTeoria({s:0, l:0, a:2}, {s:0, l:1, a:2}), 2);
    assert.equal(testarTeoria({s:0, l:2, a:2}, {s:0, l:1, a:2}), 2);
  });

  it('should return 3 when the weapon is incorrect', function() {
    assert.equal(testarTeoria({s:0, l:1, a:0}, {s:0, l:1, a:2}), 3);
    assert.equal(testarTeoria({s:0, l:1, a:1}, {s:0, l:1, a:2}), 3);
  });

  it('should return 2 or 3 when the suspect is right but not the others.', function() {
    assert.notEqual([2, 3].indexOf(testarTeoria({s:0, l:2, a:0}, {s:0, l:1, a:2})), -1);
  });

  it('should return 1 or 3 when the place is right but not the others.', function() {
    assert.notEqual([1, 3].indexOf(testarTeoria({s:1, l:1, a:0}, {s:0, l:1, a:2})), -1);
  });

  it('should return 1 or 2 when the weapon is right but not the others.', function() {
    assert.notEqual([1, 2].indexOf(testarTeoria({s:1, l:2, a:2}, {s:0, l:1, a:2})), -1);
  });

  it('should return 1, 2 or 3 when any try is right.', function() {
    assert.notEqual([1, 2, 3].indexOf(testarTeoria({s:4, l:5, a:6}, {s:0, l:1, a:2})), -1);
  });

  it('should return the correct solution', function() {
    assert.deepEqual(descobrirTeoria({s:1, l:1, a:1}), {s:1, l:1, a:1});
    assert.deepEqual(descobrirTeoria({s:3, l:2, a:7}), {s:3, l:2, a:7});
  })
});