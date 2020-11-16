$var = 10; 
sub returnfunction {  
    return $var;  
} 
sub dynamicscopingfunction{  
    local $var = 20;  
    return returnfunction();  
} 
print "Static Scope: " + returnfunction() ."\n";
print "Dynamic Scope: " + dynamicscopingfunction();
