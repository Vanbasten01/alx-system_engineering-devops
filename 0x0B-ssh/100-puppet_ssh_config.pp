# a Puppet manifest to make changes to our configuration file.
include stdlib
file_line {'privat key identity':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentifyFile ~/.ssh/school',
}

file_line { 'no password authentication':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAutentication  no',
}
