from frontend.models import Client, Domain

# create your public tenant
tenant = Client(
    schema_name='account',
    name='Account Inc.',
    paid_until='2016-12-05',
    on_trial=False,
    type='public'
)

tenant.save()

domain = Domain()
domain.domain = 'account.localhost' # don't add your port or www here! on a local server you'll want to use localhost here
domain.tenant = tenant
domain.is_primary = True
domain.save()
