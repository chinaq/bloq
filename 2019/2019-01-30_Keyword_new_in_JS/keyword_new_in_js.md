# [new operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)

The new operator lets developers create an instance of a user-defined object type or of one of the built-in object types that has a constructor function.The new keyword does the following things:

- Creates a blank, plain JavaScript object;
- Links (sets the constructor of) this object to another object;
- Passes the newly created object from Step 1 as the this context;
- Returns this if the function doesn't return its own object.

总之，new 将返回一个 this 对象