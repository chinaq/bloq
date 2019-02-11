# Functional Instantiation pattern

```js
const eater = () => ({})
const sleeper = () => ({})
const player = () => ({})
const barker = () => ({})
const meower = () => ({})
const adopter = () => ({})
const friender = () => ({})

function Cat (name, energy, declawed) {
  this.name = name
  this.energy = energy
  this.declawed = declawed

  return Object.assign(
    this,
    eater(this),
    sleeper(this),
    player(this),
    meower(this),
  )
}

const charles = new Cat('Charles', 10, false)
```

可视为 interface 在 JS 中的实现