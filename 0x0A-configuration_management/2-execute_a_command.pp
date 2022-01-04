# Kill a process by name
exec { 'pkill killmenow':
    command => 'pkill killmenow',
}