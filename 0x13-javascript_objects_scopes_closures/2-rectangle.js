#!/usr/bin/node

class Rectangle {
  if (w <= 0 || h <= 0) {
     return {};
  }
        
  this.width = w;
  this.height = h;
}   
module.exports = Rectangle;
