import {
    create,
    type CredentialCreationOptionsJSON,
} from "@github/webauthn-json";
import { useNavigate } from "react-router-dom";


import { Button } from "@/components/ui/button";
import { toast } from "sonner"



const Dashboard = () => {
    const navigate = useNavigate();
    const handleLogout = async () => {
        try {
            const response = await fetch('http://localhost:8000/logout', {
                credentials: 'include',
            });
            const data = await response.json();
            if (response.ok) {
                console.log('Logout successful:', data);
                navigate('/login');
            } else {
                console.error('Logout failed:', data.message);
            }
        } catch (error) {
            console.error('Logout error:', error);
        }
    };

    async function registerPasskey() {
        const createOptionsResponse = await fetch("http://localhost:8000/passkey/start-registration", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            credentials: 'include',
        });

        const createOptions = await createOptionsResponse.json();
        console.log("createOptions", createOptions)

        const credential = await create(
            createOptions as CredentialCreationOptionsJSON,
        );
        console.log(credential)

        const response = await fetch("http://localhost:8000/passkey/finalize-registration", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            credentials: "include",
            body: JSON.stringify(credential),
        });
        console.log(response)

        if (response.ok) {
            toast.success("Registered passkey successfully!");
            return;
        }
    }
    return (
        <div className="p-4">
            <h1>Dashboard</h1>
            <Button onClick={handleLogout}>Logout</Button>
            <div>
                <Button
                    onClick={() => registerPasskey()}
                    className="flex justify-center items-center space-x-2 mt-8"
                >
                    Register a new passkey
                </Button>
            </div>
        </div>
    )
}

export default Dashboard;