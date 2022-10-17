Summary:	A Kubernetes credential (exec) plugin implementing azure authentication
Name:		kubelogin
Version:	0.0.20
Release:	1
License:	MIT
Group:		Applications
Source0:	https://github.com/Azure/kubelogin/releases/download/v%{version}/%{name}-linux-amd64.zip
# Source0-md5:	20f2c2e90da09b71a611844ccc8b4ca6
URL:		https://github.com/Azure/kubelogin
ExclusiveArch:	%{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to put there
%define		_enable_debug_packages	0

%description
This is a client-go credential (exec) plugin implementing azure
authentication.

This plugin provides features that are not available in kubectl. It is
supported on kubectl v1.11+

Features
- convert-kubeconfig command to converts kubeconfig with existing
  azure auth provider format to exec credential plugin format
- device code login _ non-interactive service principal login
- non-interactive user principal login using Resource owner login flow
- non-interactive managed service identity login
- non-interactive Azure CLI token login (AKS only)
- non-interactive workload identity login
- AAD token will be cached locally for renewal in device code login
  and user principal login (ropc) flow. By default, it is saved in
  ~/.kube/cache/kubelogin/
- addresses kubernetes/kubernetes#86410 to remove spn: prefix in
  audience claim, if necessary. (based on kubeconfig or commandline
  argument --legacy)
- Setup for Kubernetes OIDC Provider using Azure AD

%prep
%setup -qc
mv bin/linux_*/kubelogin .

%build
./kubelogin --version

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
