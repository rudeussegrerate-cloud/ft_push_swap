*This project has been created as part of the 42 curriculum by \<login\>.*

---

# Born2beRoot

## Description

Born2beRoot est un projet d'administration système du cursus 42. L'objectif est de configurer une machine virtuelle serveur sous **Debian** en appliquant des règles strictes de sécurité : partitionnement chiffré via LVM, politique de mots de passe renforcée, configuration de sudo, pare-feu UFW, et service SSH. Un script de monitoring bash est également mis en place pour afficher les informations système en temps réel sur tous les terminaux.

Ce projet initie aux fondamentaux de l'administration Linux : gestion des utilisateurs, des groupes, des services, et de la sécurité système.

---

## Project Description

### Choix du système d'exploitation : Debian

**Debian** a été choisi pour ce projet pour les raisons suivantes :

**Avantages de Debian :**
- Distribution stable, mature et largement documentée
- Gestionnaire de paquets `apt` simple et puissant
- AppArmor intégré et facile à configurer
- Recommandé par le sujet pour les débutants en administration système
- Grande communauté, nombreuses ressources disponibles

**Inconvénients de Debian :**
- Cycle de mise à jour plus lent (stabilité prioritaire sur la nouveauté)
- Moins répandu dans les environnements entreprise Red Hat

---

### Comparaisons techniques

#### Debian vs Rocky Linux

| Critère | Debian | Rocky Linux |
|---|---|---|
| Base | Debian (indépendant) | RHEL (Red Hat) |
| Gestionnaire de paquets | `apt` / `dpkg` | `dnf` / `rpm` |
| Sécurité MAC | AppArmor | SELinux |
| Pare-feu | UFW / iptables | firewalld |
| Public cible | Général / serveurs | Entreprise / production |
| Complexité | Modérée | Élevée |

**Rocky Linux** est un successeur communautaire de CentOS, conçu pour les environnements d'entreprise. Il est plus complexe à configurer (notamment SELinux) mais très proche de ce qu'on retrouve en production dans les grandes infrastructures.

---

#### AppArmor vs SELinux

| Critère | AppArmor | SELinux |
|---|---|---|
| Modèle | Basé sur les chemins de fichiers | Basé sur les labels (contextes) |
| Facilité de config | Plus simple | Plus complexe |
| Utilisé sur | Debian, Ubuntu | Rocky, Fedora, RHEL |
| Granularité | Moyenne | Très fine |
| Profils | Par application | Par processus et fichier |

**AppArmor** fonctionne en associant des profils de sécurité aux applications, en limitant ce qu'elles peuvent faire. **SELinux** utilise un système d'étiquettes (labels) sur chaque fichier et processus, offrant un contrôle plus granulaire mais nécessitant une expertise plus poussée.

---

#### UFW vs firewalld

| Critère | UFW | firewalld |
|---|---|---|
| Syntaxe | Simple et lisible | Basée sur des zones |
| Utilisation | Debian / Ubuntu | Rocky / Fedora / RHEL |
| Backend | iptables / nftables | nftables / iptables |
| Modification à chaud | Oui | Oui |
| Courbe d'apprentissage | Faible | Modérée |

**UFW** (Uncomplicated Firewall) est conçu pour simplifier la gestion d'iptables. **firewalld** utilise un système de zones réseau plus flexible, adapté aux environnements complexes.

---

#### VirtualBox vs UTM

| Critère | VirtualBox | UTM |
|---|---|---|
| Plateformes | Windows, Linux, macOS (Intel) | macOS (Intel + Apple Silicon) |
| Architecture | x86 / x86_64 | x86_64, ARM (via émulation) |
| Gratuité | Oui | Oui |
| Interface | Graphique | Graphique |
| Apple Silicon | Non natif | Oui (natif) |

**VirtualBox** est la solution recommandée sur la majorité des machines. **UTM** est l'alternative utilisée sur les Mac Apple Silicon (M1/M2/M3) qui ne supportent pas VirtualBox nativement.

---

### Choix de conception principaux

#### Partitionnement (LVM chiffré)

Le disque est partitionné avec au minimum 2 partitions chiffrées via **LVM** (Logical Volume Manager) :

```
sda
├── sda1       /boot        (non chiffré)
├── sda2       (extended)
└── sda5_crypt (chiffré)
    ├── LVMGroup-root     /
    ├── LVMGroup-swap     [SWAP]
    └── LVMGroup-home     /home
```

LVM permet de gérer les volumes logiques de manière flexible (redimensionnement, snapshots). Le chiffrement (via LUKS) protège les données en cas d'accès physique à la machine.

#### Politique de mots de passe

Configurée via `/etc/login.defs` et `libpam-pwquality` :

- Expiration tous les **30 jours**
- Délai minimum entre changements : **2 jours**
- Avertissement **7 jours** avant expiration
- Longueur minimale : **10 caractères**
- Doit contenir : 1 majuscule, 1 minuscule, 1 chiffre
- Maximum **3 caractères identiques consécutifs**
- Ne doit pas contenir le nom d'utilisateur
- Doit contenir au moins **7 nouveaux caractères** par rapport au précédent (hors root)

#### Configuration sudo

Fichier : `/etc/sudoers.d/<login>`

- Maximum **3 tentatives** en cas de mauvais mot de passe
- Message d'erreur personnalisé
- Logs complets dans `/var/log/sudo/`
- Mode **TTY** activé
- Chemins `secure_path` restreints

#### Gestion des utilisateurs

- Utilisateur `<login>` appartenant aux groupes `user42` et `sudo`
- Connexion SSH **root interdite**
- SSH sur **port 4242** uniquement

#### Services installés

- **SSH** : openssh-server (port 4242, PermitRootLogin no)
- **UFW** : pare-feu avec uniquement le port 4242 ouvert
- **AppArmor** : actif au démarrage
- **cron** : pour l'exécution automatique du script monitoring

---

## Instructions

### Prérequis

- VirtualBox (ou UTM sur Mac Apple Silicon)
- Image ISO Debian (dernière version stable)
- Minimum 8 Go d'espace disque recommandé

### Installation de la VM

1. Créer une nouvelle VM dans VirtualBox (type : Linux, version : Debian 64-bit)
2. Allouer RAM (1024 Mo minimum), créer un disque virtuel (8-12 Go)
3. Démarrer avec l'ISO Debian, suivre l'installation guidée
4. Lors du partitionnement, choisir **"Utiliser tout le disque avec LVM chiffré"**
5. Appliquer les configurations décrites ci-dessous

### Configuration post-installation

```bash
# Mise à jour du système
su -
apt update && apt upgrade -y

# Installation des paquets nécessaires
apt install -y sudo ufw openssh-server libpam-pwquality apparmor

# Ajout de l'utilisateur au groupe sudo et user42
usermod -aG sudo,user42 <login>

# Configuration SSH (port 4242, pas de root)
nano /etc/ssh/sshd_config
# -> Port 4242
# -> PermitRootLogin no
systemctl restart ssh

# Activation UFW
ufw allow 4242
ufw enable
```

### Script monitoring.sh

Placé dans `/usr/local/bin/monitoring.sh`, exécuté toutes les 10 minutes via cron :

```bash
# Activer dans crontab root :
crontab -e
# Ajouter :
*/10 * * * * /usr/local/bin/monitoring.sh
```

Pour interrompre sans modifier le script :
```bash
# Désactiver le job cron temporairement
crontab -e
# Commenter ou supprimer la ligne */10 * * * *
```

### Obtenir la signature du disque (soumission)

```bash
# Sur Linux :
sha1sum ~/VirtualBox\ VMs/<nom_vm>/<nom_vm>.vdi > signature.txt

# Sur macOS :
shasum ~/VirtualBox\ VMs/<nom_vm>/<nom_vm>.vdi > signature.txt
```

Placer `signature.txt` et ce `README.md` à la racine du dépôt Git.

> ⚠️ Ne jamais inclure le fichier `.vdi` dans le dépôt Git.

---

## Resources

### Documentation officielle

- [Documentation Debian](https://www.debian.org/doc/)
- [Manuel Debian — Administration système](https://www.debian.org/doc/manuals/debian-reference/ch01.fr.html)
- [LVM HowTo (tldp.org)](https://tldp.org/HOWTO/LVM-HOWTO/)
- [UFW — Ubuntu Help](https://help.ubuntu.com/community/UFW)
- [AppArmor Wiki](https://gitlab.com/apparmor/apparmor/-/wikis/home)
- [PAM Password Quality (pam_pwquality)](https://linux.die.net/man/8/pam_pwquality)
- [sudoers man page](https://www.sudo.ws/docs/man/sudoers.man/)
- [Cron — man page](https://man7.org/linux/man-pages/man5/crontab.5.html)
- [wall — man page](https://man7.org/linux/man-pages/man1/wall.1.html)

### Articles et tutoriels

- [The Linux Command Line (book)](https://linuxcommand.org/tlcl.php)
- [ArchWiki — LVM](https://wiki.archlinux.org/title/LVM)
- [ArchWiki — dm-crypt / LUKS](https://wiki.archlinux.org/title/Dm-crypt)
- [DigitalOcean — How To Set Up a Firewall with UFW on Debian](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-debian-10)

### Utilisation de l'IA

L'IA (Claude) a été utilisée pour les tâches suivantes dans ce projet :

- **Rédaction du README** : structure, comparaisons techniques (AppArmor vs SELinux, Debian vs Rocky, etc.) et mise en forme Markdown
- **Compréhension des concepts** : explication de LVM, LUKS, PAM, sudoers en termes accessibles
- **Vérification de syntaxe** : relecture des configurations bash et des commandes shell

L'IA n'a pas été utilisée pour : la configuration effective de la VM, l'écriture du script `monitoring.sh`, ni pour les décisions d'architecture — toutes réalisées manuellement et comprises de façon autonome.
