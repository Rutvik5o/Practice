<%@ Page Language="C#" AutoEventWireup="true"  CodeFile="Default.aspx.cs" Inherits="_Default" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Untitled Page</title>
    <style type="text/css">
        .style1
        {
            width: 100%;
            height: 100px;
        }
        .style2
        {
            width: 574px;
        }
        .style3
        {
            width: 574px;
            height: 22px;
        }
        .style4
        {
            height: 22px;
        }
        .style5
        {
            height: 23px;
        }
        .style6
        {
            height: 23px;
            width: 154px;
        }
        .style7
        {
            width: 154px;
        }
        .style8
        {
            height: 23px;
            width: 256px;
        }
        .style9
        {
            width: 256px;
        }
        .style10
        {
            width: 190px;
        }
        .style11
        {
            height: 23px;
            width: 190px;
        }
        .style12
        {
            height: 24px;
            width: 154px;
        }
        .style13
        {
            height: 24px;
            width: 256px;
        }
        .style14
        {
            height: 24px;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
        <asp:Panel ID="Panel1" runat="server" Height="172px">
        <strong>Personal Details    
            <br />
            <br />
            </strong>
        
            <table class="style1">
                <tr>
                    <td class="style3">
                        FirstName:</td>
                    <td class="style4">
                        <asp:TextBox ID="TextBox1" runat="server" Width="173px"></asp:TextBox>
                    </td>
                </tr>
                <tr>
                    <td class="style2">
                        LastName:</td>
                    <td>
                        <asp:TextBox ID="TextBox2" runat="server" Width="173px"></asp:TextBox>
                    </td>
                </tr>
                <tr>
                    <td class="style2">
                        Email:</td>
                    <td>
                        <asp:TextBox ID="TextBox3" runat="server" Width="173px"></asp:TextBox>
                    </td>
                </tr>
                <tr>
                    <td class="style2">
                        Phone Number:</td>
                    <td>
                        <asp:TextBox ID="TextBox4" runat="server" Width="173px"></asp:TextBox>
                    </td>
                </tr>
            </table>
        </asp:Panel>
    
    </div>
    <asp:Panel ID="Panel2" runat="server" Height="186px">
        <strong>Education Details:</strong>
        <br />
        <br />
        <table class="style1">
            <tr>
                <td class="style12">
                </td>
                <td class="style13">
                    Universty/Board</td>
                <td class="style13">
                    Passing Year</td>
                <td class="style14">
                    Percentage Obtained</td>
            </tr>
            <tr>
                <td class="style7">
                    S.S.C.</td>
                <td class="style9">
                    <asp:TextBox ID="TextBox5" runat="server" Width="118px"></asp:TextBox>
                </td>
                <td class="style9">
                    <asp:TextBox ID="TextBox9" runat="server" Width="118px"></asp:TextBox>
                </td>
                <td>
                    <asp:TextBox ID="TextBox13" runat="server" Width="118px"></asp:TextBox>
                </td>
            </tr>
            <tr>
                <td class="style7">
                    H.S.C.</td>
                <td class="style9">
                    <asp:TextBox ID="TextBox6" runat="server" Width="118px"></asp:TextBox>
                </td>
                <td class="style9">
                    <asp:TextBox ID="TextBox10" runat="server" Width="118px"></asp:TextBox>
                </td>
                <td>
                    <asp:TextBox ID="TextBox14" runat="server" Width="118px"></asp:TextBox>
                </td>
            </tr>
            <tr>
                <td class="style6">
                    Under Graduate</td>
                <td class="style8">
                    <asp:TextBox ID="TextBox7" runat="server" Width="118px"></asp:TextBox>
                </td>
                <td class="style8">
                    <asp:TextBox ID="TextBox11" runat="server" Width="118px"></asp:TextBox>
                </td>
                <td class="style5">
                    <asp:TextBox ID="TextBox15" runat="server" Width="118px"></asp:TextBox>
                </td>
            </tr>
            <tr>
                <td class="style7">
                    Post Graduate</td>
                <td class="style9">
                    <asp:TextBox ID="TextBox8" runat="server" Width="118px"></asp:TextBox>
                </td>
                <td class="style9">
                    <asp:TextBox ID="TextBox12" runat="server" Width="118px"></asp:TextBox>
                </td>
                <td>
                    <asp:TextBox ID="TextBox18" runat="server" Width="115px"></asp:TextBox>
                </td>
            </tr>
        </table>
    </asp:Panel>
    <asp:Panel ID="Panel3" runat="server" Height="172px">
       <strong>Experience Details:</strong>
        <br />
        <br />
        <br />
        <table class="style1">
            <tr>
                <td class="style10">
                    Company Name:</td>
                <td>
                    <asp:TextBox ID="TextBox16" runat="server"></asp:TextBox>
                </td>
            </tr>
            <tr>
                <td class="style11">
                    From Date:</td>
                <td class="style5">
                    <asp:TextBox ID="TextBox17" runat="server"></asp:TextBox>
                </td>
            </tr>
            <tr>
                <td class="style10">
                    To Date:</td>
                <td>
                    <asp:TextBox ID="TextBox19" runat="server"></asp:TextBox>
                </td>
            </tr>
            <tr>
                <td class="style10">
                    Post:</td>
                <td>
                    <asp:TextBox ID="TextBox20" runat="server"></asp:TextBox>
                </td>
            </tr>
        </table>
        <br />
        <asp:Panel ID="Panel4" runat="server">
            <asp:Button ID="Button1" runat="server" onclick="Button1_Click" Text="Submit" />
        </asp:Panel>
    </asp:Panel>
    </form>
</body>
</html>
