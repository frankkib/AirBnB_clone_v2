# static web puppet code deplyment
package { 'nginx':
  ensure => installed,
}
file { '/data':
  recurse => true,
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0777',
}
file { '/data/web_static':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0777'
}
file { '/data/web_static/releases':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0777',
}
file { '/data/web_static/shared':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0777',
}
file { '/data/web_static/releases/test':
  ensure => directory, 
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0777',
}
file { '/data/web_static/releases/test/index.html':
  content => '<html><body> Holberton School</body></html>',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0777',
}
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0777',
}
file { '/etc/nginx/sites-available/default':
  ensure  => present
  replace => true
  content =>  "
server {
    listen 80;
    listen [::]:80 default_server;
    server_name _;
    location /hbnb_static {
        alias /data/web_static/current/;
    }
    error_page 404 /404.html;
    location = /404.html {
        internal;
        root /usr/share/nginx/html;
    }
}
"
}
service { 'nginx'
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/enginx/sites-available/default'],
}
