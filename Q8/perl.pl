$var = 0; 
sub returnfunction {  
    return $var;  
} 
sub dynamicscopingfunction{  
    local $var = 1;  
    return returnfunction();  
}
sub staticscopingfunction{
   my $var = 1;
   return returnfunciton()
} 
print "Static Scope: " + returnfunction() ."\n";
print "Dynamic Scope: " + dynamicscopingfunction() . “\n”;
print “Another Static Scope: ” + staticscopingfunction() . “\n”; 
