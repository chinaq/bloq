# ABP Data Seed

- create tenant - `TenantAppService.CreateAsync`
- dataSeeder.Seed - `DataSeeder.SeedAsync`
    - each seederContribute.seed - `IDataSeedContributor.SeedAsync`
        - identity seeder - `IdentityDataSeedContributor`
          - role seeder
          - user sedder
        - permission seeder - `PermissionDataSeedContributor`
        - identity server seeder - `IdentityServerDataSeedContributor`
        - domain data seeder - `MyProjectNameDataSeedContributor`