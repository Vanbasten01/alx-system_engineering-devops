#a puppet manifest to fix a typo
exec { 'fix_typo':
        command  => 'sed -i s/\.phpp/\.php/g /var/www/html/wp-settings.php',
        provider => 'shell'
}
