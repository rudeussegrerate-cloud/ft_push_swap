#include "module/utile.h"
#include "module/data.h"

t_data *parsing(char* arg[])
{
    t_data *param = malloc(sizeof(t_data));
    if (param == NULL)
        return NULL;
    int i = 0;
    while (arg[i])
    {
        if (atoi(arg[i]) != 0 && atoi(arg[i]) == 1)
        {
            param->num_coders = atoi(arg[i]);
            // param.time_to_burnout = 
            // param.time_to_compile = 
            // param.time_to_debug = 
            // param.time_to_refactor = 
            // param.num_compiles_req = 
            // param.dongle_cooldown = 
            // param.scheduler_type = 
        }
        else
            return NULL;
        i++;
    }
    printf("%d", param->num_coders);
    return param;
}
