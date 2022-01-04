# Puppet task advanced ssh
file { 'config' :
  ensure  => 'file',
  path    => '~/.ssh/config',
  owner   => 'root',
  group   => 'root',
  mode    => '0600',
  content => 'Host 35.196.79.133
  User ubuntu
  IdentifyFile ~/.ssh/school'
}