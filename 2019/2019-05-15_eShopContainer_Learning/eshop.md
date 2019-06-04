# eShopContainer Learning
### learning examples form micosoft

# Preparing
### set up
- if on mac, please set `IdentityUrl` in `docker-compose.override.yml`
``` yml
IdentityUrl=http://docker.for.mac.localhost:5105
# Local Mac: Use http://docker.for.mac.localhost:5105
# || Local Windows:  Use 10.0.75.1 in a "Docker for Windows" environment, if using "localhost" from browser.
# || Remote access: Use ${ESHOP_EXTERNAL_DNS_NAME_OR_IP} if using external IP or DNS name from browser.
```
- While `microsoft/mssql-server-linux` is not inited correctly after `docker-compose up`, please rm it and `docker-compose` again.

### compare with commits to understand the dev process
- `git log --skip 3000` to get the commits list needed
- `git checkout 8cc57c25421d9` to check out the node for clean comparing by vs code git history tools

## Learning
### Day 1 - Aggrgate & SeedWork
- DDD only found in Ordering Service

![Aggregate](./img/Aggregate.png)

### Day 2 - procession on order

```
webmvc

1
  -> cart.controller.index
  -> cart.view.index [checkout]

2
  -> cart.controller.index.post
  -> order.controller.create
  -> basket.service.getOrderDraft
    ->> api.purchase.getOrderDraft
      ->>> orderClient.GetOrderDraft
  -> order.view.create [place order]

3
  -> order.controller.checkout
  -> basket.service.checkout
    ->> api.basket.CheckoutBasket
      ->>> eventBus.publish(checkoutEvent)
  -> order.view.index [detail]
```

![1.cart](./img/1.cart.png)  
![2.checkedout](./img/2.checkedout.png)  
![3.created](./img/3.created.png)  
![4.detal.png](./img/4.detail.png)  