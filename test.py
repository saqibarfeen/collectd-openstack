import creds

from NovaMetrics import NovaMetrics
from CinderMetrics import CinderMetrics
from NeutronMetrics import NeutronMetrics

c=creds.get_creds()
n=NovaMetrics(c['auth_url'],c['username'],c['password'],c['project_name'],c['project_domain_id'],c['user_domain_id'])
cinder=CinderMetrics(c['auth_url'],c['username'],c['password'],c['project_name'],c['project_domain_id'],c['user_domain_id'])
neutron=NeutronMetrics(c['auth_url'],c['username'],c['password'],c['project_name'],c['project_domain_id'],c['user_domain_id'])
n.collect_limit_metrics()
