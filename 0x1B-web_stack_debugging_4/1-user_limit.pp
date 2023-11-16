#increase holberton user limit
exec { 'increase-hard-file-limit':
  command  => 'sed -i "/holberton hard/s/5/5000/" /etc/security/limits.conf',
  provider => shell
}

exec { 'increase-soft-file-limit':
  command  => 'sed -i "/holberton soft/s/4/4000/" /etc/security/limits.conf',
  provider => shell
}
