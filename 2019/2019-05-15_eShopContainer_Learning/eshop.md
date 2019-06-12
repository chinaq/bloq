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

### Day 3
- Domain Event 在 context.save 中 publish
- CQRS 是 await 到 query 或 command 结果
- 以上两者，均采用 mediatR

### Day 4
- add buyer
```
Order

-> ValidateOrAddBuyerAggregateWhenOrderStartedDomainEventHandler
  -> buyer.VerifyOrAddPaymentMethod
  -> buyerRepo.Save
  -> orderingIntegrationEventService.AddAndSaveEventAsync
```

### Day 5
- about EventBus

![event bus](./img/EventBus.jpeg)

- unusual `AutoFac` Interface Setting on eventBus in `Ordering.API` project

``` cs
// ApplicationModule.cs

builder
  .RegisterAssemblyTypes(typeof(CreateOrderCommandHandler).GetTypeInfo().Assembly)
  .AsClosedTypesOf(typeof(IIntegrationEventHandler<>))
```

``` cs
// Startup.cs

private void ConfigureEventBus(IApplicationBuilder app)
{
    var eventBus = app.ApplicationServices.GetRequiredService<IEventBus>();

    eventBus.Subscribe<OrderStatusChangedToAwaitingValidationIntegrationEvent, OrderStatusChangedToAwaitingValidationIntegrationEventHandler>();
    eventBus.Subscribe<OrderStatusChangedToPaidIntegrationEvent, OrderStatusChangedToPaidIntegrationEventHandler>();
    eventBus.Subscribe<OrderStatusChangedToStockConfirmedIntegrationEvent, OrderStatusChangedToStockConfirmedIntegrationEventHandler>();
    eventBus.Subscribe<OrderStatusChangedToShippedIntegrationEvent, OrderStatusChangedToShippedIntegrationEventHandler>();
    eventBus.Subscribe<OrderStatusChangedToCancelledIntegrationEvent, OrderStatusChangedToCancelledIntegrationEventHandler>();
    eventBus.Subscribe<OrderStatusChangedToSubmittedIntegrationEvent, OrderStatusChangedToSubmittedIntegrationEventHandler>();
}
```

- about init in `Startup.cs`
  - `EventBusRabbitMQ`: AddSingleton
  - `MediatR`: registered in MediatorModule, not need to set singleton


  ### Day 6
  - 从购物车中 checkout
```
UserCheckoutAcceptedIntegrationEventHandler
  -> mediator.send CreateOrderCommand

CreateOrderCommandHander.Handle
  -> orderingIntegrationEventService.AddAndSaveEventAsync
  -> orderReposity.Add

In TransactionBehaviour
    -> ordringIntegrationEventService.PulishEventsThroughEventBusAsync
```

![behavior](./img/behavior.jpeg)