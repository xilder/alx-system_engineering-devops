include stdlib

file_line { 'change identity_file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '	IdentityFile ~/.ssh/school',
 replace => true,
}

file_line { 'turn off pwd auth':
  ensure   => present,
  path     => '/etc/ssh/ssh_config',
  line     => '	PasswordAuthentication no',
   replace => true,
}
