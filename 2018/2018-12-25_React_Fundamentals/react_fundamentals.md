# React Fundamentals


## Intro to the React Ecosystem
- notes
    - [tylermcginnis/react-fundamentals/Notes.md](https://github.com/tylermcginnis/react-fundamentals/blob/master/Notes.md)
- project
    - [Curriculum for React Fundamentals Course](https://github.com/tylermcginnis/react-fundamentals-curriculum)
    - ![](https://cloud.githubusercontent.com/assets/2933430/21000853/3c9b2bbe-bcda-11e6-88b8-3619aa319bcd.png)
- exercise
    - [tylermcginnis/react-fundamentals]( https://github.com/tylermcginnis/React-Fundamentals)
    - ![](https://cloud.githubusercontent.com/assets/2933430/26085553/7dac7a1e-39a2-11e7-830a-9011505b5958.png)

## Setting up your first React component with NPM, Babel, and Webpack
- NPM
    - intall module
- Webpack
    - code bundler: make production and development transformations to the code
    - three steps:
        - starting point of your application, or your root JavaScript file. 
        - which transformations to make on your code. 
        - which location it should save the new transformed code.
- Babel
    - a wonderful tool for compiling your JavaScript.
- The Usage
  - NPM -> Webpack -> Babel

## Dataflow with Props
- props
- .map
- .filter

## Pure Functions. f(d)=v.Props and Nesting React Components.
- Components
- PropTypes

## The "this" keyword + Managing and Updating State
- Implicit Binding: 
  - object has a property which equals to a function and within that functions body one can refer to other properties of that object with this.dotNotation
- Explicit Binding: 
  - binding using functions’ in-built functionality .call, .apply, .bind.
- New/Window Binding: 
  - when we use new to create an instance of an object, it binds the this keyword to itself within any of its methods/properties.
- ES2015 Arrow Functions
  - always use the value of `this` from the enclosing scope
  - ref: [React & Autobinding](https://medium.com/komenco/react-autobinding-2261a1092849)

## Stateless Functional Components
- stateless functional components
- private components