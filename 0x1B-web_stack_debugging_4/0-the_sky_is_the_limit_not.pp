#modify the file only if necessary
exec { 'replace_line':
  command  => 'sed -i "s|ULIMIT=\"-n 15\"|ULIMIT=\"-n 10000\"|" /etc/default/nginx',
  provider => 'shell',
  unless   => 'grep -q "ULIMIT=\"-n 10000\"" /etc/default/nginx',
}

#restart NGINX only if the file is modified
service { 'nginx':
  ensure     => 'running',
  enable     => true,
  subscribe  => Exec['replace_line'],
}
