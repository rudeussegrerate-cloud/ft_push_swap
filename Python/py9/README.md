*This project has been created as part of the 42 curriculum by tusandri.*

---

## Description

Born2beRoot is a system administration project from the 42 curriculum. The goal is to set up a secure server inside a virtual machine, following strict rules: encrypted partitions with LVM, SSH hardening, firewall configuration, strong password policies, sudo restrictions, and an automated monitoring script running every 10 minutes.

---

## Project description

### Operating System Choice: Debian

**Debian** was chosen over Rocky Linux for the following reasons:

- Explicitly recommended by the subject for beginners in system administration
- AppArmor (default on Debian) is simpler to configure than SELinux (default on Rocky)
- Very large community and extensive documentation
- Stable, well-tested packages

**Debian disadvantage:** package versions tend to be older than on rolling-release distributions.

**Rocky Linux disadvantage:** more complex to set up (SELinux, firewalld), targeted at enterprise environments — not ideal for a first Linux administration project.

---

### Main design choices

**Partitioning — LVM + LUKS encryption**

At least 2 encrypted partitions were created using LVM. LVM allows resizing partitions without reinstalling the OS. LUKS encryption (`sda5_crypt`) protects data at rest: if the disk is stolen, the data remains unreadable.

**Security policies**

- SSH running exclusively on port 4242 — root login disabled
- UFW firewall active at startup, only port 4242 open
- Strong password policy: 30-day expiry, minimum 2 days between changes, 7-day warning, minimum 10 characters (uppercase + lowercase + digit), no more than 3 consecutive identical characters, username not allowed in password
- sudo: limited to 3 attempts, custom error message, all inputs/outputs logged to `/var/log/sudo/`, TTY mode required, restricted secure_path
- AppArmor running at startup

**User management**

- Non-root user `tusandri` belonging to groups `user42` and `sudo`
- hostname: `tusandri42`

**Partitionning**
```bash
NAME               MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINTS
sda                  8:0    0 30.1G  0 disk  
├─sda1               8:1    0  476M  0 part  /boot
├─sda2               8:2    0    1K  0 part  
└─sda5               8:5    0 29.6G  0 part  
  └─sda5_crypt     254:0    0 29.6G  0 crypt 
    ├─LVM-root     254:1    0  9.3G  0 lvm   /
    ├─LVM-swap     254:2    0  2.1G  0 lvm   [SWAP]
    ├─LVM-home     254:3    0  4.7G  0 lvm   /home
    ├─LVM-var      254:4    0  2.8G  0 lvm   /var
    ├─LVM-srv      254:5    0  2.8G  0 lvm   /srv
    ├─LVM-tmp      254:6    0  2.8G  0 lvm   /tmp
    └─LVM-var--log 254:7    0  5.1G  0 lvm   /var/log
sr0                 11:0    1 1024M  0 rom
```
---

### Debian vs Rocky Linux

| Criteria | Debian | Rocky Linux |
|---|---|---|
| Target audience | Beginner-friendly | Enterprise-oriented |
| Security module | AppArmor | SELinux |
| Package manager | APT / Aptitude | DNF |
| Community | Very large | Growing |
| Recommended by subject | ✅ Yes | ❌ No |

---

### AppArmor vs SELinux

| | AppArmor | SELinux |
|---|---|---|
| Default on | Debian | Rocky / RHEL |
| Approach | Path-based profiles | Label-based (inode) |
| Complexity | Simple | Complex but very powerful |
| Weakness | Breaking if file is moved | Steep learning curve |

AppArmor controls access based on file paths and uses plain-text profiles. SELinux attaches security labels to every file and process — more robust, but significantly harder to manage.

---

### UFW vs firewalld

| | UFW | firewalld |
|---|---|---|
| Default on | Debian / Ubuntu | Rocky / Fedora |
| Syntax | Very simple | Zone-based, more complex |
| Dynamic reload | No | Yes |

UFW is a simplified frontend for `iptables`, designed for clarity. firewalld uses "zones" for granular network control and suits more complex environments.

---

### VirtualBox vs UTM

| | VirtualBox | UTM |
|---|---|---|
| Platform | Windows / Linux / macOS | macOS only |
| Apple Silicon (M1/M2) | Limited | Native (ARM) |
| Open source | Partial | Yes |

VirtualBox was used for this project. It is the standard choice on x86/amd64 machines. UTM is the preferred alternative for Mac M1/M2 users since VirtualBox has poor performance on ARM.

---

## Feature list

- ✅ Encrypted LVM partitions (LUKS)
- ✅ SSH server on port 4242 (root login disabled)
- ✅ UFW firewall — only port 4242 open
- ✅ Strong password policy (expiry, complexity, history)
- ✅ sudo hardening (attempts limit, logging, TTY, secure_path)
- ✅ AppArmor running at startup
- ✅ Non-root user in `user42` and `sudo` groups
- ✅ `monitoring.sh` script broadcasting system info every 10 minutes via `wall`
- ✅ hostname set to `tusandri42`

---

## Technical choices

| Component | Choice | Reason |
|---|---|---|
| OS | Debian (latest stable) | Recommended for beginners, large community |
| Hypervisor | VirtualBox | Standard on x86/amd64, well-supported at 42 |
| Partitioning | LVM + LUKS encryption | Flexibility + data protection at rest |
| Firewall | UFW | Simple syntax, sufficient for this project |
| Security module | AppArmor | Default on Debian, path-based and easy to manage |
| SSH | OpenSSH on port 4242 | Standard, port changed for security |
| Password policy | libpam-pwquality + login.defs | Native Debian tools, no extra dependency |
| Monitoring | bash + cron + wall | Lightweight, no external tools required |

---

## Usage examples

### Connect via SSH
```bash
ssh tusandri@<vm_ip> -p 4242
```

### Check system status
```bash
# Partitions
lsblk

# AppArmor
sudo /usr/sbin/aa-status

# Firewall
sudo ufw status verbose

# SSH port
ss -tunlp | grep 4242

# Password policy for a user
sudo chage -l tusandri

# sudo logs
cat /var/log/sudo/sudo.log
```

### Run monitoring script manually
```bash
bash /usr/local/bin/monitoring.sh
```

### User management
```bash
# Create a new user
sudo adduser newuser

# Create a group
sudo groupadd newgroup

# Add user to group
sudo usermod -aG newgroup newuser

# Verify groups
groups newuser
```

### Cron — stop/restart monitoring without modifying the script
```bash
# Edit cron as root
sudo crontab -e
# Comment or delete the line to stop it:
# */10 * * * * /usr/local/bin/monitoring.sh | wall
```

---

## Instructions

### Prerequisites
- VirtualBox (or UTM for Mac M1/M2) installed
- Debian ISO — latest stable version (no testing/unstable)

### Setup

1. Create a new VM in VirtualBox (≥ 8 GB disk, ≥ 1 GB RAM)
2. Boot from Debian ISO → choose **Install** (no graphical interface allowed)
3. Partitioning: choose **Manual** → create encrypted LVM partitions

```bash
# SSH — port 4242, no root login
sudo nano /etc/ssh/sshd_config
# Port 4242
# PermitRootLogin no
sudo systemctl restart ssh

# Firewall
sudo apt install ufw
sudo ufw allow 4242/tcp
sudo ufw enable

# Password policy
sudo apt install libpam-pwquality
sudo nano /etc/security/pwquality.conf
sudo nano /etc/login.defs
sudo chage -M 30 -m 2 -W 7 tusandri
sudo chage -M 30 -m 2 -W 7 root

# sudo hardening
sudo visudo
# Defaults passwd_tries=3
# Defaults badpass_message="Wrong password. Access denied."
# Defaults logfile="/var/log/sudo/sudo.log"
# Defaults log_input, log_output
# Defaults requiretty
# Defaults secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"
```

4. Create `monitoring.sh` and schedule it with cron every 10 minutes via `wall`

### Verification

```bash
lsblk                        # partitions
/usr/sbin/aa-status          # AppArmor
sudo ufw status verbose      # firewall
ss -tunlp | grep 4242        # SSH port
sudo chage -l tusandri       # password policy
```

---

## Resources

- [Debian official site](https://www.debian.org/index.fr.html)
- [AppArmor on Debian — wiki](https://wiki.debian.org/AppArmor/HowToUse)
- [SELinux vs AppArmor — comparison](https://tuxcare.com/fr/blog/selinux-vs-apparmor/)
- [OpenSSH server configuration](https://www.it-connect.fr/chapitres/openssh-configuration-du-serveur-ssh/)
- [SSH command examples](https://www.geeksforgeeks.org/linux-unix/ssh-command-in-linux-with-examples/)

### AI usage

Claude (claude.ai) was used during this project for the following tasks:
- **Understanding concepts:** differences between APT/Aptitude, AppArmor/SELinux, UFW/firewalld
- **Clarifying LVM + LUKS encryption** interaction during partitioning
- **Structuring the README** according to the subject requirements (Chapter VI)

All configuration choices were applied and understood manually. AI was used as a learning aid, not as a replacement for reasoning through the project.
