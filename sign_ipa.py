import os
import subprocess

def sign_ipa(ipa_path, certificate_name, provisioning_profile):
    """
    Sign an IPA file using Fastlane.
    :param ipa_path: Path to the IPA file.
    :param certificate_name: Name of the signing certificate.
    :param provisioning_profile: Path to the provisioning profile.
    """
    try:
        command = [
            'fastlane', 'sigh', 'resign',
            ipa_path,
            '--signing_identity', certificate_name,
            '--provisioning_profile', provisioning_profile
        ]
        subprocess.run(command, check=True)
        print("IPA signed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error signing IPA: {e}")

# Example usage
sign_ipa(
    ipa_path='YourApp.ipa',
    certificate_name='iPhone Developer: Your Name (TEAMID)',
    provisioning_profile='YourApp.mobileprovision'
)