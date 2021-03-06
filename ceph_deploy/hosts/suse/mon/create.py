from ceph_deploy.hosts import common
from ceph_deploy.lib.remoto import process


def create(distro, args, monitor_keyring):
    hostname = distro.conn.remote_module.shortname()
    common.mon_create(distro, args, monitor_keyring, hostname)

    process.run(
        distro.conn,
        [
            'rcceph',
            '-c',
            '/etc/ceph/{cluster}.conf'.format(cluster=args.cluster),
            'start',
            'mon.{hostname}'.format(hostname=hostname)
        ],
        timeout=7,
    )
