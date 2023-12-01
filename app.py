from app import createApp, db, Routes

app1 = createApp('application')
application = app1  # Agrega esta línea

app1.register_blueprint(Routes.UsersRoutes.userMain)
app1.register_blueprint(Routes.authRoutes.authMain)
app1.register_blueprint(Routes.TicketsRoutes.ticketsMain)
app1.register_blueprint(Routes.DistributorRoutes.distributorsMain)
app1.register_blueprint(Routes.HostingRoutes.hostingsMain)
app1.register_blueprint(Routes.DomainRoutes.domainsMain)
app1.register_blueprint(Routes.BuyoutRoutes.buyoutsMain)
app1.register_blueprint(Routes.CategoryRoutes.categoriesMain)
app1.register_blueprint(Routes.CountryRoutes.countriesMain)
app1.register_blueprint(Routes.PayModeRoutes.payModesMain)
app1.register_blueprint(Routes.PayPlanRoutes.payPlansMain)
app1.register_blueprint(Routes.PlanRoutes.plansMain)
app1.register_blueprint(Routes.PlatformRoutes.platformsMain)
app1.register_blueprint(Routes.RolRoutes.rolsMain)
app1.register_blueprint(Routes.CreditCardRoute.creditCardsMain)

if __name__ == '__main__':
    with app1.app_context():
        db.create_all() 

    app1.run()