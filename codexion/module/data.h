#ifndef DATA_H
#define DATA_H

#include <sys/time.h>
#include "utile.h"

typedef struct s_data
{
    int         num_coders;          // number_of_coders
    long long   time_to_burnout;     // time_to_burnout (en ms)
    long long   time_to_compile;     // time_to_compile (en ms)
    long long   time_to_debug;       // time_to_debug (en ms)
    long long   time_to_refactor;    // time_to_refactor (en ms)
    int         num_compiles_req;    // number_of_compiles_required
    long long   dongle_cooldown;     // dongle_cooldown (en ms)
    int         scheduler_type;      // Un flag (ex: 1 pour FIFO, 2 pour EDF)
    
    // Éléments de synchronisation globale
    long long   start_time;          // Timestamp du début de la simulation
    int         simulation_end;      // Drapeau (0 = en cours, 1 = terminé)
    pthread_mutex_t write_mutex;     // Mutex pour sérialiser les logs (éviter les mélanges)
    pthread_mutex_t state_mutex;     // Mutex pour protéger les variables partagées (ex: simulation_end)
}   t_data;






#endif
