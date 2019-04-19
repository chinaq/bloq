# React Router

- version > 4.0 more react like
- [`Route.children`](https://reacttraining.com/react-router/web/api/Route/children-func)
  - Sometimes you need to render whether the path matches the location or not.
``` jsx
<ul>
  <ListItemLink to="/somewhere" />
  <ListItemLink to="/somewhere-else" />
</ul>;

const ListItemLink = ({ to, ...rest }) => (
  <Route
    path={to}
    children={({ match }) => (
      <li className={match ? "active" : ""}>
        <Link to={to} {...rest} />
      </li>
    )}
  />
);
```
  