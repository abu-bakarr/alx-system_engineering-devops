#  Strace is your friend
exec { 'change-now':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => '/bin/'
}
