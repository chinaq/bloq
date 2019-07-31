# React Hooks

## Why React Hooks?
- **(1) why** and for what **(2) benefit**
- cause better on
    - State
    - Lifecycle methods
    - Sharing non-visual logic

## Managring State with Hooks
- The useState Hook

## Adding Side Effects
- The `useEffect` Hook
- `useEffect` vs Lifecycle Events
    -  You don’t need to know anything about the traditional lifecycle methods to understand `useEffect`. 
    -  `useEffect` is just a new way of adding lifecycle events to our function components.

## Custom Hooks
- [React Higher-Order Components](https://tylermcginnis.com/react-higher-order-components/)
- [React Render Props](https://tylermcginnis.com/react-render-props/)
- sharing non-visual logic via a custom Hook is THE thing that makes Hooks so special.

## Managing (Complex) State
- `useReducer`
    - If different pieces of state update independently from one another (hovering, selected, etc.), `useState` should work fine. 
    - If your state tends to be updated together or if updating one piece of state is based on another piece of state, go with `useReducer`.
