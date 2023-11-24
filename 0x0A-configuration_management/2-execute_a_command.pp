# kills a peocess
exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
