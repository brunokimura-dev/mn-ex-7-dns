# Mininet DNS Example Setup

This project demonstrates a hierarchical DNS configuration using BIND9 within a Mininet emulated network. 

## DNS Hierarchy and Network Topology

![Network topology](dns-topo.jpg)

---

## 1. Launch Your Vagrant VM

Make sure your VM is set up and running with:

```bash
vagrant reload
vagrant ssh
```

---

## 2. Install BIND DNS Server

Inside the VM, install the DNS service:

```bash
sudo apt-get update
sudo apt-get install bind9
```

---

## 3. Navigate to Your Workstation Folder

```bash
cd /workstation/
```

---

## 4. Clone This DNS Example and Run Mininet

```bash
git clone https://github.com/brunokimura-dev/mn-ex-7-dns.git
cd mn-ex-7-dns/
sh mininet_run.sh mn-ex-dns.py
```

You should see `www1` pinging `www2` and vice versa if DNS resolution is working properly.

---

## 5. Check the DNS Configurations

After launching Mininet, test DNS resolution from one domain to another using `dig`:

### Example Commands (from the Mininet prompt):

```bash
mininet> www1 dig www2.xyz.org @195.0.0.10
mininet> www1 dig www2.xyz.org @195.0.0.21
mininet> www1 dig www2.xyz.org @195.0.0.31
mininet> www1 dig www2.xyz.org @195.0.0.32
```

### Expected Output:

```
. . .
;; ANSWER SECTION:
www2.xyz.org.        60000    IN    A    195.0.0.42
. . .
```

This confirms that name resolution for `www2.xyz.org` works through the DNS hierarchy.

---

