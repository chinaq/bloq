# Semantic UI React Test

- Modals must be rendered to the document body
    - [Jest snapshots not working with some Semantic-UI-React components](https://stackoverflow.com/questions/48373732/jest-snapshots-not-working-with-some-semantic-ui-react-components)

``` js
// testing by @testing-library/react
// and check from document

......
const yesBtn = await waitForElement(() => document.querySelector('button.ui.green.inverted'));
......
```