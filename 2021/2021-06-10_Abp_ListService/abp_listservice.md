# Abp 中 Angular 的 ListService 使用多字段 sort

- 依据官方 issue 示例，可以使用 sort
  ``` js
  sort(data) {
    const { prop, dir } = data.sorts[0];
    this.list.sortKey = prop;
    this.list.sortOrder = dir;
  }
  ```
  - [Replace the abp-tables with the ngx-datatable #4198](https://github.com/abpframework/abp/issues/4198)
- 依据官方 source 和 tests 示例，可以看到排序文本是直接将 sortKey 和 sortOrder 组合
  ``` js
  sorting: this._sortOrder ? `${this._sortKey} ${this._sortOrder}` : undefined
  ```
  - [`list.service.ts` source code](https://github.com/abpframework/abp/blob/48c52625f4c4df007f04d5ac6368b07411aa7521/npm/ng-packs/packages/core/src/lib/services/list.service.ts)
  - [`list.service.spec.ts` test code](https://github.com/abpframework/abp/blob/48c52625f4c4df007f04d5ac6368b07411aa7521/npm/ng-packs/packages/core/src/lib/tests/list.service.spec.ts)
- 虽然没有官方多字段 sort 示例，但直接手动赋值多字段可行
  ``` js
  this.list.sortKey = "name asc, age";
  this.list.sortOrder = "desc";
  this.list.QueryOrDoSthElse();
  ```