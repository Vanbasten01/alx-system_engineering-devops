#a Puppet manifest that kills a process named 'killmenow'.

exec { 'kill_killmenow_process':
  command => 'pkill killmenow',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'pgrep killmenow',
  returns  => [0, 1],
}
