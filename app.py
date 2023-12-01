from app import createApp, db

app1 = createApp('development')

from app.Routes.UsersRoutes import userMain
from app.Routes.authRoutes import authMain
from app.Routes.TicketsRoutes import ticketsMain
from app.Routes.DistributorRoutes import distributorsMain
from app.Routes.HostingRoutes import hostingsMain
from app.Routes.DomainRoutes import domainsMain
from app.Routes.BuyoutRoutes import buyoutsMain
from app.Routes.CategoryRoutes import categoriesMain
from app.Routes.CountryRoutes import countriesMain
from app.Routes.PayModeRoutes import payModesMain
from app.Routes.PayPlanRoutes import payPlansMain
from app.Routes.PlanRoutes import plansMain
from app.Routes.PlatformRoutes import platformsMain
from app.Routes.RolRoutes import rolsMain
from app.Routes.CreditCardRoute import creditCardsMain

app1.register_blueprint(userMain)
app1.register_blueprint(authMain)
app1.register_blueprint(ticketsMain)
app1.register_blueprint(distributorsMain)
app1.register_blueprint(hostingsMain)
app1.register_blueprint(domainsMain)
app1.register_blueprint(buyoutsMain)
app1.register_blueprint(categoriesMain)
app1.register_blueprint(countriesMain)
app1.register_blueprint(payModesMain)
app1.register_blueprint(payPlansMain)
app1.register_blueprint(plansMain)
app1.register_blueprint(platformsMain)
app1.register_blueprint(rolsMain)
app1.register_blueprint(creditCardsMain)

if __name__ == '__main__':
    with app1.app_context():
        db.create_all() 

    app1.run()



